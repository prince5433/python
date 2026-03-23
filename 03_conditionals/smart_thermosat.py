device_status="active"
temperature=38

if device_status == "active":
    # pass  # come back to this
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")