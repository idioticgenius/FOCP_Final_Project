import sys

def process_log(log_file):
    """
    Process the log file to extract relevant information.

    Parameters:
    - log_file (file): The file object containing the log data.

    Returns:
        Dictionary: {
            "count_our_cat": count_our_cat,
            "count_their_cat": count_their_cat,
            "total_time_stayed": total_time_stayed,
            "longest_visit_time": longest_visit_time,
            "shortest_visit_time": shortest_visit_time
        }
    """    
    count_their_cat = 0
    count_our_cat = 0
    total_time_stayed = 0
    longest_visit_time = 0
    shortest_visit_time = float('inf')
     
    # Read all lines from the log file
    data = log_file.readlines()
    
    # Iterate over each line in the log file   
    for line in data:
        # Split each line into words using ',' as a delimiter
        word = line.strip().split(',')
        
        # Check the category and update counters accordingly
        if word[0] == 'THEIRS':
            count_their_cat += 1
        elif word[0] == 'OURS':
            count_our_cat += 1
            # Calculate the time stayed by subtracting entered time from leaving time
            time_stayed = int(word[2]) - int(word[1])
            total_time_stayed += time_stayed

            # Calculate longest and shortest visit times
            longest_visit_time = max(longest_visit_time, time_stayed)
            shortest_visit_time = min(shortest_visit_time, time_stayed)

    return {
        "count_our_cat": count_our_cat,
        "count_their_cat": count_their_cat,
        "total_time_stayed": total_time_stayed,
        "longest_visit_time": longest_visit_time,
        "shortest_visit_time": shortest_visit_time
    }

def display_results(stats):
    """
    Display the results of the log file analysis.

    Parameters:
    - count_our_cat (int): Count of visits by OUR cat.
    - count_their_cat (int): Count of visits from  THEIR cat.
    - total_time_stayed (int): Total time spent by our cat in the shelter.
    - longest_visit_time (int): Duration of the longest visit.
    - shortest_visit_time (int): Duration of the shortest visit.
    """    
    BOX_WIDTH = 45
    print("=" * (BOX_WIDTH + 3))
    print(f"|{'Log File Analysis':^{BOX_WIDTH + 1}}|")
    print("=" * (BOX_WIDTH + 3))
    print(f"|{'Cat Visits:':<25}{stats['count_our_cat']:<21}|")
    print(f"|{'Other Cats:':<25}{stats['count_their_cat']:<21}|")

    print("=" * (BOX_WIDTH + 3))
    print(f"|{'Total Time in House:':<25}{stats['total_time_stayed'] // 60} Hours, {stats['total_time_stayed'] % 60:<2} {'Minutes':<9}|")
    print("=" * (BOX_WIDTH + 3))

    # Display average visit length only if OUR cat visits
    if stats["count_our_cat"] > 0:
        print(f"|{'Average Visit Length:':<25}{stats['total_time_stayed'] // stats['count_our_cat']:<2} Minutes{'|':>12}")
    else:
        print(f"|{'Average Visit Length:':<25}{0:<3} Minutes|")

    print(f"|{'Longest Visit Time:':<25}{stats['longest_visit_time']:} Minutes{'|':>12}")
    print(f"|{'Shortest Visit Time:':<25}{stats['shortest_visit_time']:<2} Minutes{'|':>12}")
    print("=" * (BOX_WIDTH + 3))

def main():
    """
    Main function
    """
    try:
        log_file = sys.argv[1]
        with open(log_file, "r") as log_file:
            # Process
            stats = process_log(log_file)
        display_results(stats)

    except IndexError:
        print("Missing command line argument")
    except FileNotFoundError:
        print(f"Cannot open '{log_file}'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    



if __name__ == '__main__':
    main()