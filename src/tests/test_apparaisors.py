from fastapi.testclient import TestClient
from app.main import app
from unittest import mock

client = TestClient(app)

def test_install_firmware():
    # Mocking the dependencies and the database
    with mock.patch("app.api.repositories.apparaisor.get_one") as mock_get_one, \
         mock.patch("app.api.repositories.batch.get_one") as mock_get_batch, \
         mock.patch("app.api.repositories.apparaisor.update_installed_firmware") as mock_update_installed_firmware:

        # Set up the mocks
        mock_get_one.return_value = MockAppraisor()
        mock_get_batch.return_value = MockBatch()

        # Make a request to the API endpoint
        response = client.put("/apparaisors/1/install-firmware", json={"firmware_version": "1.0"})

        # Assertions
        assert response.status_code == 200
        assert response.json() == {"message": "Firmware installed successfully"}

        # Verify that the update_installed_firmware function was called with the correct arguments
        mock_update_installed_firmware.assert_called_once_with(1, "1.0")

# Mock classes for testing
class MockAppraisor:
    def __init__(self):
        self.id = 1
        self.batch_id = 1

class MockBatch:
    def __init__(self):
        self.firmware = ["1.0"]
