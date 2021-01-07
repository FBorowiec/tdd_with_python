import pytest


class FizzBuzz:
    def fizz_buzz(self, value):
        if self.is_multiple(value, 3):
            if self.is_multiple(value, 5):
                return "FizzBuzz"
            return "Fizz"
        if self.is_multiple(value, 5):
            return "Buzz"
        return str(value)

    def is_multiple(self, value, mod):
        return (value % mod) == 0


class TestFizzBuzz:
    @classmethod
    def setup_class(cls):
        print("Setup TestFizzBuzz!")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestFizzBuzz!")

    def test_returns_1_with_1_passed_to_FizzBuzz(self):
        ret = FizzBuzz().fizz_buzz(1)
        assert ret == "1"

    def test_returns_2_with_2_passed_to_FizzBuzz(self):
        ret = FizzBuzz().fizz_buzz(2)
        assert ret == "2"

    def test_returns_Fizz_with_3_passed_to_FizzBuzz(self):
        ret = FizzBuzz().fizz_buzz(3)
        assert ret == "Fizz"

    def test_returns_Fizz_with_5_passed_to_FizzBuzz(self):
        ret = FizzBuzz().fizz_buzz(5)
        assert ret == "Buzz"

    def test_returns_FizzBuzz_with_15_passed_to_FizzBuzz(self):
        ret = FizzBuzz().fizz_buzz(15)
        assert ret == "FizzBuzz"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
