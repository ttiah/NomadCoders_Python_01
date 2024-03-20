def save_to_file(file_name, jobs):
    with open(f'{file_name}.csv', 'w') as f:
        f.write('Title,Company,Reward,Link\n')

        for job in jobs:
            f.write(f"{job['title']},{job['company']},{job['reward']},{job['link']}\n")
