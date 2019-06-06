import calculator


class TestCalculator:


	def test_addition(self):
		assert 4 == calculator.add(2, 2)


	def test_subtraction(self):
		assert 2 == calculator.subtract(4, 2)


	def test_multiplication(self):
		assert 10 == calculator.multiply(10, 1)


	def test_division(self):
		assert 8 == calculator.divisy(16,2)