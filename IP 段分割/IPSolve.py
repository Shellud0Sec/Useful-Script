start_ip, end_ip = input("请输入 IP 范围（格式为 xxx.xxx.xxx.xxx-xxx）：").split('-')

start_ip_parts = list(map(int, start_ip.split('.')))
end_ip_parts = list(map(int, end_ip.split('.')))

ips = []
while start_ip_parts != end_ip_parts:
    ips.append('.'.join(map(str, start_ip_parts)))
    start_ip_parts[-1] += 1
    for i in range(3, 0, -1):
        if start_ip_parts[i] == 256:
            start_ip_parts[i] = 0
            start_ip_parts[i-1] += 1

ips.append('.'.join(map(str, start_ip_parts)))

for ip in ips:
    print(ip)
