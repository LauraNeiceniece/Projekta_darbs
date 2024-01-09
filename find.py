import sys

if __name__ == "__main__":
    # Check if three command line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python find.py <region> <max-rent> <min-room-count> <order-col>")
    else:

        # TODO: IF check for int values
        # Assign argument values to variables
        region = sys.argv[1]
        maxRent = int(sys.argv[2])
        minRoomCount = int(sys.argv[3])
        orderCol = sys.argv[4]

        # Print the variables
        print("reģions:", region)
        print("max Īre:", maxRent)
        print("min Istabu skaits :", minRoomCount)
        print("secības kolonna:", orderCol)
