import sys



def process_log(log_file):
    count_their_cat = 0
    count_our_cat = 0
    total_time_stayed = 0
    longest_visit_time = 0
    shortest_visit_time = float('inf')
    
    data = log_file.readlines()
    for line in data:
        word = line.strip().split(',')
        if word[0] == 'THEIRS':
            count_their_cat += 1
        elif word[0] == 'OURS':
            count_our_cat += 1
            time_stayed = int(word[2]) - int(word[1])
            total_time_stayed += time_stayed

            if time_stayed > longest_visit_time:
                longest_visit_time = time_stayed
            if time_stayed < shortest_visit_time:
                shortest_visit_time = time_stayed
    return count_our_cat, count_their_cat, total_time_stayed, longest_visit_time, shortest_visit_time

def display_results(count_our_cat, count_their_cat, total_time_stayed, longest_visit_time, shortest_visit_time):
        print("Log File Analysis")
        print("="*20)
        print(f"\nCat Visits: {count_our_cat}")
        print(f"Other Cats: {count_their_cat}")
        print(f"\nTotal Time in House(Our Cat): {total_time_stayed//60} Hours, {total_time_stayed%60} Minutes")
        
        if count_our_cat > 0:
            print(f"\nAverage Visit Length: {total_time_stayed//count_our_cat} Minutes")
        else:
            print(f"\nAverage Visit Length: 0 Minutes")


        print(f"Longest Visit: {longest_visit_time} Minutes")
        print(f"Shortest Visit: {shortest_visit_time} Minutes")

def main():
    try:
        log_file = sys.argv[1]
        with open(log_file, "r") as log_file:
            count_our_cat, count_their_cat, total_time_stayed, longest_visit_time, shortest_visit_time = process_log(log_file)

        display_results(count_our_cat, count_their_cat, total_time_stayed, longest_visit_time, shortest_visit_time)

    except IndexError:
        print("Missing command line argument")
    except FileNotFoundError:
        print(f"Cannot open '{log_file}'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    



if __name__ == '__main__':
    main()