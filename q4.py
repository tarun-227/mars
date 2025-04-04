
def muchiko_filter(data, window_size):#filter to find average for that range of window size

    smoothed_data = []
    for i in range(len(data) - window_size + 1):
        set_of_elements = data[i: i + window_size]
        smoothed_data.append(sum(set_of_elements) // window_size)#calculating average and adding to result list
    return smoothed_data
def sanchiko_filter(data, window_size):#finds median
    filtered_data = []
    for i in range(len(data) - window_size + 1):
        set_of_elements = sorted(data[i : i + window_size])
        if window_size % 2 == 1:
            filtered_data.append(set_of_elements[window_size // 2])  #if window is odd, take middle value
        else:
            # if window is even, take average of two middle values (// for integer division)
            filtered_data.append((set_of_elements[window_size // 2 - 1] + set_of_elements[window_size // 2]) // 2)
    return filtered_data

sensor_data = list(map(int, input("Enter sensor readings separated by spaces: ").split()))
window_size = int(input("Enter window size: "))

muchiko_result = muchiko_filter(sensor_data, window_size)
sanchiko_result = sanchiko_filter(sensor_data, window_size)

# Apply Hybrid filter only if enough elements exist
if len(muchiko_result) >= window_size:
    hybrid_result = sanchiko_filter(muchiko_result, window_size)
else:
    hybrid_result = muchiko_result  # If not enough elements, return Muchiko result as-is

print("Muchiko Filter:", muchiko_result)
print("Sanchiko Filter:", sanchiko_result)
print("Hybrid Filter:", hybrid_result)
