import os
import subprocess
import pdb

command_base = 'cmd \k {}'
comment_string = '<!-- comment to trigger first translation -->\n'
# command_cd = '"cd \"C:\\Users\\Vincent De Clercq\\OneDrive - Hexagon\\Documents\\smartling\\git test\\full-test\""'
# os.system(command_base.format(command_cd))
command_main = 'git checkout main'
os.system(command_main)
command_branch_base = 'git checkout -b '
command_push_upstream_base = 'git push --set-upstream origin '
command_commit = 'git commit -a -m \"adding comment to trigger translation\"'
command_push = 'git push'
branch_base = 'initial-'
command_pr_base = 'gh pr create --title {} --fill'

# g = Github("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")
# repo = g.get_repo("vincentdcq6/full-test")
pr_title_base = 'first translation for '

# pdb.set_trace()

# os.walk folder
folder = 'C:\\Users\\Vincent De Clercq\\OneDrive - Hexagon\\Documents\\smartling\\git test\\full-test\\Documentation\\en\\_guides\\BIM_whats_new_V21'
base_name = 'C:\\Users\\Vincent De Clercq\\OneDrive - Hexagon\\Documents\\smartling\\git test\\full-test\\Documentation\\en\\'
#folder = 'C:\\Users\\Vincent De Clercq\\OneDrive - Hexagon\\Documents\\shizzle\\BCAD_whats_new_V21'
for root, dirs, files in os.walk(folder):
	for f in files:
		lines = []
		newlines = []
		full_path = "{}\\{}".format(root, f)
		print(full_path)

#		checkout new branch
		branch = branch_base + f
		branch = branch.split('.')[0]
		branch = branch.replace('_','-')
		command_branch = command_branch_base + branch
		print(command_branch)
		os.system(command_branch)

		# pdb.set_trace()

#		push --set-upstream origin new branch
		command_push_upstream = command_push_upstream_base + branch
		print(command_push_upstream)
		os.system(command_push_upstream)

#		add comment to file
		with open(full_path, 'r', encoding='utf-8') as fp:
			lines = fp.readlines()

		newlines.append(lines[0])
		newlines.append(comment_string)
		for i in range(1,len(lines)):
			newlines.append(lines[i])

		with open(full_path, 'w', encoding='utf-8') as fp:
			fp.writelines(newlines) 

#		commit
		print(command_commit)
		os.system(command_commit)

#		push
		print(command_push)
		os.system(command_push)

#		create pull request using api
		pr_title = full_path.replace(base_name,'')
		pr_title = pr_title.replace('\\','/')
		command_pr = command_pr_base.format(pr_title)
		print(command_pr)
		os.system(command_pr)

#		checkout main
		print(command_main)
		os.system(command_main)

