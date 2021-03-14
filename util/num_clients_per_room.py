from urllib.request import urlopen

pusher_url = "https://pusher.wa.binary-kitchen.de"
room = "_/global/das-labor.github.io/workadv_das-labor/main.json"

metrics_url = pusher_url + "/metrics"

with urlopen(metrics_url) as f:
    lines = f.readlines()

for line in lines:
    line_str = line.decode()
    if room in line_str:
        # line of format
        # workadventure_nb_clients_per_room{room="_/global/das-labor.github.io/workadv_das-labor/main.json"} -280
        num = int(line_str.split(' ')[1])

print(num, "clients online")