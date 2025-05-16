# Validation experiment 2

This experiment evaluates the performance of a modeling platform under stress using the **ModelFed protocol**.

We designed a scenario where an admin user creates a model and executes multiple modeling activities that are federated to several users. The tests incrementally increase the number of federated users to **5**, **10**, and **20**, in order to assess scalability and responsiveness.

### Test Scenarios

Three JMeter test plans are included in the `jmeter/` directory, corresponding to each user load level:

- 5 federated users
- 10 federated users
- 20 federated users

### 📊 Results

All collected performance data and generated graphs are documented in the [`results.xlsx`](./results.xlsx) file.