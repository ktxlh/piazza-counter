"""
Author: Shang-Ling Hsu (https://github.com/ktxlh)
"""
##############################################################################
#                               Configurations                               #
##############################################################################
# See Piazza URL for your IDs: https://piazza.com/class/<class_id>?cid=<cid>
class_id = "ky3a26n35u1bv"
cids = [54, 59, 62, 63]
output_fname = "Reading Responses 03-02 to 03-16.csv"
##############################################################################

from piazza_api import Piazza
import pandas as pd

p = Piazza()
p.user_login()

class_p = p.network(class_id)
users = class_p.get_all_users()

students = list(filter(lambda x: x['role'] == 'student', users))
students = list(filter(lambda x: len(x['name']) > 0, students))
student_uid_map = {x['id']: x['name'] for x in students}

names = list(set(map(lambda x: x['name'], students)))  # deduplicate
names.sort(key=lambda x: x)  # sort by full name
names.sort(key=lambda x: x.split()[-1])  # sort by last name
name_idx_map = {x: i for i, x in enumerate(names)}

df = pd.DataFrame({'names': names})

sum_scores = [0 for _ in range(len(df))]
for cid in cids:
    post = class_p.get_post(cid)
    subject = post['history'][-1]['subject']
    scores = [0 for _ in range(len(df))]
    for child in post["children"]:
        idx = name_idx_map[student_uid_map[child['uid']]]
        admin_endorses = list(filter(lambda x: x['admin'], child['tag_good']))
        scores[idx] = len(admin_endorses) + 1
        sum_scores[idx] += len(admin_endorses) + 1
    df[subject] = scores
df['sum'] = sum_scores

df.to_csv(output_fname, header=True, index=False)
