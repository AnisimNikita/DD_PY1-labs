def find_common_participants(group_1, group_2, separator=','):
    participants_1 = set(group_1.split(separator))
    participants_2 = set(group_2.split(separator))

    common_participants = participants_1.intersection(participants_2)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants1 = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники с разделителем '|':", common_participants1)

participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_participants2 = find_common_participants(participants_first_group_comma, participants_second_group_comma)
print("Общие участники с запятой по умолчанию:", common_participants2)

