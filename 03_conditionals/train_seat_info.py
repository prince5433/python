seat_type = input("Enter seat type (sleeper / ac / general / luxury): ").lower()

match seat_type:
    case "sleeper":
        print("No AC, beds available")
    case "ac":
        print("Air conditioned, comfy ride")
    case "general":
        print("Cheapest option, no reservation")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")