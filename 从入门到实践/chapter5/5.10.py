current_users=['yn','fo','si','so','ju']
new_users=['Si','So','jj','pp','s*']
for a in new_users:
    if a.lower() in current_users :
        print('in',a)
    else:
        print('not in',a)
