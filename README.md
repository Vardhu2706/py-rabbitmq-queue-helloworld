# RabbitMQ Tutorial #1 - Hello World (Python)

This is the first tutorial in the RabbitMQ series: **Hello World!**  
We’ll write two small Python programs: a **Producer** that sends a message and a **Consumer** that receives and prints it.

---

## Overview
- **Producer (P):** Sends messages to the `hello` queue.
- **Queue:** Acts as a message buffer managed by RabbitMQ.
- **Consumer (C):** Receives messages from the `hello` queue.

Diagram:

```
[P] ---> [hello queue] ---> [C]
```

---

## Requirements
- Python 3.x
- RabbitMQ server (running locally or remotely)
- Pika (Python client for RabbitMQ)

Install Pika:
```bash
python -m pip install pika --upgrade
```

---

## Running the Example
1. Start RabbitMQ server.
2. Run the producer script to send a message:
   ```bash
   python send.py
   ```
3. Run the consumer script to receive messages:
   ```bash
   python receive.py
   ```

---

## Reference
Official tutorial: [RabbitMQ - Tutorial One (Python)](https://www.rabbitmq.com/tutorials/tutorial-one-python#hello-world)