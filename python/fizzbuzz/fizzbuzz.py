def convert_to_fizzbuzz (input_int):
	output_str = 'Fizz' if (input_int % 3 == 0) else ''
	output_str += 'Buzz' if (input_int % 5 == 0) else ''
	return output_str if len(output_str) > 0 else str(input_int)