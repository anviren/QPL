import random
import time
from threading import Thread

class AdaptiveData:
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def adapt(value):
        return AdaptiveData(value)
    
    def interpret(self, context):
        if context.get("mode") == "string":
            return str(self.value)
        elif context.get("mode") == "int":
            return int(self.value)
        return self.value

class Process:
    def __init__(self, name, context=None):
        self.name = name
        self.context = context if context else {}
        self.state = None

    def execute(self, data):
        self.state = data
        self.run()

    def run(self):
        pass

class SuperpositionState:
    def __init__(self, states):
        self.states = states

    def collapse(self, context):
        if context.get("traffic_density", 0) > 70:
            return "red"
        elif context.get("traffic_density", 0) > 40:
            return "yellow"
        else:
            return "green"

class TrafficSensorProcess(Process):
    def run(self):
        while True:
            traffic_data = self.collect_data()
            self.state = traffic_data
            time.sleep(1)
    
    def collect_data(self):
        traffic_density = random.randint(0, 100)
        print(f"Sensor: Traffic density is {traffic_density}")
        return AdaptiveData.adapt({"traffic_density": traffic_density})

class TrafficLightProcess(Process):
    def run(self):
        traffic_state = SuperpositionState(["green", "yellow", "red"])
        while True:
            if self.context.get("sensor_process"):
                sensor_data = self.context["sensor_process"].state
                if sensor_data:
                    interpreted_data = sensor_data.interpret(self.context)
                    current_state = traffic_state.collapse(interpreted_data)
                    self.execute(current_state)
                    time.sleep(self.context.get("time_delay", 5))
    
    def execute(self, state):
        self.state = state
        print(f"Traffic Light: Current state is {self.state.upper()}")

class QuantumProgram:
    def __init__(self):
        self.processes = []
    
    def add_process(self, process):
        self.processes.append(process)
    
    def start(self):
        for process in self.processes:
            thread = Thread(target=process.run)
            thread.start()

def main():
    quantum_program = QuantumProgram()

    sensor_process = TrafficSensorProcess("TrafficSensorProcess")
    traffic_light_process = TrafficLightProcess("TrafficLightProcess", context={'sensor_process': sensor_process, "time_delay": 5})
    
    quantum_program.add_process(sensor_process)
    quantum_program.add_process(traffic_light_process)

    quantum_program.start()

if __name__ == "__main__":
    main()
