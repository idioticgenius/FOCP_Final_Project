import sys
count_their_cat = 0
count_our_cat = 0
total_time_stayed = 0
average_visit_time = 0
longest_visit_time = 0
shortest_visit_time = float('inf')

def main():
    global count_their_cat, count_our_cat, total_time_stayed, longest_visit_time, shortest_visit_time
    try:
        log_file = sys.argv[1]
        with open(log_file, "r") as log_file:
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
                

        print(f"Cat Visits: {count_our_cat}")
        print(f"Other Cats: {count_their_cat}")
        print(f"Total Time in House: {total_time_stayed//60} Hours, {total_time_stayed%60} Minutes")
        print(f"Average Visit Length: {total_time_stayed//count_our_cat} Minutes")
        print(f"Longest Visit: {longest_visit_time} Minutes")
        print(f"Shortest Visit: {shortest_visit_time} Minutes")

    except IndexError:
        print("Missing command line argument")
    except FileNotFoundError:
        print(f"Cannot open '{log_file}'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    



if __name__ == '__main__':
    main()