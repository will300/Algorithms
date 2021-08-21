memos = {}

def cancel_appointments(arr, num_minutes=0, prev_app=False):

    # Adjacent appointments cannot both run, so at least one must be cancelled
    # If there is a previous appointment you must cancel the next one
    if len(arr) == 0:
        return num_minutes

    if memos.get(len(arr)):
        return memos[len(arr)]

    if prev_app:
        if len(arr) == 1:
            if memos.get(len(arr)): memos[len(arr)] = num_minutes
            return num_minutes
        else:
            result = cancel_appointments(arr[1:], num_minutes)
            if memos.get(len(arr)): memos[len(arr)] = result
            return result

    if len(arr) == 1:
        if memos.get(len(arr)): memos[len(arr)] = num_minutes + arr[0]
        return num_minutes + arr[0]

    result = max(cancel_appointments(arr[2:], num_minutes + arr[0]), \
                 cancel_appointments(arr[2:], num_minutes + arr[1], True)) 
    if memos.get(len(arr)): memos[len(arr)] = result
    return result


def test_case(arr, solution, test_func):

    output = test_func(arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case([30, 15, 60, 75, 45, 15, 15, 45], 180, cancel_appointments)
