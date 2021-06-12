from tronpy import AsyncTron as ATron


class AsyncTron(ATron):
    @staticmethod
    def is_address(address):
        try:
            return ATron.is_address(address)
        except ValueError:
            return False
