import argparse
parser = argparse.ArgumentParser()

parser.add_argument(
    "--hour", "--h", help="enter annual wage to get hourly wage", type=int)
parser.add_argument("--annual", "--a",
                    help="enter hourly wage to get annual wage", type=int)
parser.add_argument(
    "--week", "--w", help="show weekly wage", action="store_true")
parser.add_argument(
    "--month", "--m", help="show monthly wage (31 days/4 weeks)", action="store_true")
parser.add_argument(
    "--time", "--t", help="custom number of work days", type=int)

output = ""
hourly = None

args = parser.parse_args()


if args.hour != None and args.annual != None:
    print("Invalid choices, cannot have both hour and annual choices")
    exit(0)

if args.hour != None:
    hourly = args.hour / 52 / 40
    output += f'Hourly wage: {hourly}\n'
if args.annual != None:
    hourly = args.annual
    annual = hourly * 40 * 52
    output += f'Annual wage: {annual}\n'

if hourly == None:
    print("Error, you must enter wage")
    exit(0)

if args.week:
    weekly = hourly * 40
    output += f'Weekly wage: {weekly}\n'

if args.month:
    monthly = hourly * 4 * 40
    output += f'Monthly wage: {monthly}\n'

if args.time != None:
    timed = hourly * 8 * args.time
    output += f'Wage over {args.time} days: {timed}'


print(output)
