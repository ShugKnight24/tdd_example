def convert_to_fizzbuzz (input_int):
	output_str = 'Fizz' if is_fizzy(input_int) else ''
	output_str += 'Buzz' if is_buzzy(input_int) else ''
	return output_str if (len(output_str) > 0) else str(input_int)

def is_fizzy(input_int):
	return (input_int % 3 == 0) or '3' in str(input_int)

def is_buzzy(input_int):
	return (input_int % 5 == 0) or '5' in str(input_int)