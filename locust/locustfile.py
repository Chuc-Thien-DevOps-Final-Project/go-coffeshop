from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Thời gian chờ giữa các request (1 - 3 giây)

    @task
    def test_endpoint_1(self):
        self.client.get("https://opswat.chucthien.click")

    @task
    def test_endpoint_2(self):
        self.client.get("https://opswat.chucthien.click/proxy")
