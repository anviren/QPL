# Quantum Programming Language (QPL)

## Overview

The Quantum Programming Language is an advanced, process-oriented language designed to handle complex, adaptive systems where processes and data are fluid, continuous, and responsive to their context.

## Key Features

- **Processes as Primary Entities**: Execute tasks and interact dynamically.
- **Non-binary States**: Adapt processes to changing contexts.
- **Adaptive Data Types**: Flexibility in data handling.
- **Continuous Data Flow**: Real-time data processing.
- **Dynamic Interaction**: Adaptive process interaction.

## Documentation

Full documentation is available in the [docs/](./docs) folder.

## Example Program

Here's a simple example of how to use QPL:

```python
quantum_program = QuantumProgram()

data_gen_process = DataGeneratorProcess("DataGenerator")
object_manager_process = ObjectManagerProcess("ObjectManager")
adaptive_process = AdaptiveProcess("AdaptiveProcess")

quantum_program.add_process(data_gen_process)
quantum_program.add_process(object_manager_process)
quantum_program.add_process(adaptive_process)

def link_processes(gen_process, obj_process, adapt_process):
    while True:
        data = gen_process.state
        if data:
            obj_process.execute(data)
            adapt_process.execute(data)
        time.sleep(1)

thread_link = Thread(target=link_processes, args=(data_gen_process, object_manager_process, adaptive_process))
thread_link.start()

quantum_program.start()
thread_link.join()
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.