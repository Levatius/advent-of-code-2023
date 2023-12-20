import math
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Generator


class Pulse(Enum):
    LOW = 0
    HIGH = 1


@dataclass
class Signal:
    source: str
    destination: str
    pulse: Pulse


@dataclass
class BaseModule:
    name: str
    destinations: list[str]

    @staticmethod
    def process(signal: Signal) -> Pulse:
        return signal.pulse

    def output_signals_iter(self, signal: Signal) -> Generator[Signal, None, None]:
        pulse = self.process(signal)
        if pulse is not None:
            for destination in self.destinations:
                yield Signal(self.name, destination, pulse)


@dataclass
class FlipFlopModule(BaseModule):
    is_on: bool = False

    def process(self, signal: Signal) -> Pulse:
        if signal.pulse == Pulse.LOW:
            if self.is_on:
                self.is_on = False
                return Pulse.LOW
            else:
                self.is_on = True
                return Pulse.HIGH


@dataclass
class ConjunctionModule(BaseModule):
    memory: dict[str, Pulse] = field(default_factory=dict)

    def process(self, signal: Signal) -> Pulse:
        self.memory[signal.source] = signal.pulse
        if all(bool(stored_pulse.value) for stored_pulse in self.memory.values()):
            return Pulse.LOW
        return Pulse.HIGH


def get_modules(lines) -> dict[BaseModule]:
    modules = {}
    for line in lines:
        m = re.match(r"(?P<module_type>[%&]?)(?P<name>\w+) -> (?P<destinations>.+)", line)
        module_map = {"": BaseModule, "%": FlipFlopModule, "&": ConjunctionModule}
        module_type = m.group("module_type")
        name = m.group("name")
        destinations = m.group("destinations").split(", ")
        modules[name] = module_map[module_type](name, destinations)

    # Initialise conjunction modules
    for name, module in modules.items():
        if not isinstance(module, ConjunctionModule):
            continue
        for other_name, other_module in modules.items():
            if name in other_module.destinations:
                module.memory[other_name] = Pulse.LOW
    return modules


def part_1(modules, total_button_presses=1000, stop_signals=None):
    totals = {Pulse.LOW: 0, Pulse.HIGH: 0}
    cycle_lengths = []
    for button_presses in range(1, total_button_presses + 1):
        signal_queue = [Signal(source="button", destination="broadcaster", pulse=Pulse.LOW)]
        while signal_queue:
            signal = signal_queue.pop(0)

            # Used to get cycle lengths for part 2
            if stop_signals is not None:
                if signal in stop_signals:
                    stop_signals.remove(signal)
                    cycle_lengths.append(button_presses)
                if len(stop_signals) == 0:
                    return cycle_lengths

            totals[signal.pulse] += 1
            if not (module := modules.get(signal.destination)):
                continue
            signal_queue += module.output_signals_iter(signal)
    return totals[Pulse.LOW] * totals[Pulse.HIGH]


def part_2(modules):
    rx_feed_module_name = next(module.name for module in modules.values() if "rx" in module.destinations)
    sources = [module.name for module in modules.values() if rx_feed_module_name in module.destinations]
    stop_signals = [Signal(source, rx_feed_module_name, Pulse.HIGH) for source in sources]
    cycle_lengths = part_1(modules, total_button_presses=1_000_000, stop_signals=stop_signals)
    return math.lcm(*cycle_lengths)
