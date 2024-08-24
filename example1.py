from qpl import QuantumProgram, DataGeneratorProcess, ObjectManagerProcess, AdaptiveProcess

# Create an instance of QuantumProgram
quantum_program = QuantumProgram()

# Initialize processes
data_gen_process = DataGeneratorProcess("DataGenerator")
object_manager_process = ObjectManagerProcess("ObjectManager")
adaptive_process = AdaptiveProcess("AdaptiveProcess")

# Add processes to the program
quantum_program.add_process(data_gen_process)
quantum_program.add_process(object_manager_process)
quantum_program.add_process(adaptive_process)

# Link processes (define interactions)
def link_processes(gen_process, obj_process, adapt_process):
    while True:
        data = gen_process.state
        if data:
            obj_process.execute(data)
            adapt_process.execute(data)
        time.sleep(1)

# Start the program
thread_link = Thread(target=link_processes, args=(data_gen_process, object_manager_process, adaptive_process))
thread_link.start()

quantum_program.start()
thread_link.join()
