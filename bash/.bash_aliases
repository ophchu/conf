sorted-du(){
	watch -n 10 'du -s $1 | sort -nr'
}

ps-grep(){
	ps -ef | grep $1
}


ssh-ec2(){
	ssh -A  -i ~/.ssh/opr-ophir.pem hadoop@$1
}
ssh-ubuntu(){
	ssh ubuntu@$1
}

fwd-port(){
	ssh -i ~/.ssh/opr-ophir.pem -N -D 8157 hadoop@$1
}
alias psg=ps-grep
alias dus=sorted-du 
alias ec2=ssh-ec2
alias ubu=ssh-ubuntu
alias fwd=fwd-port
alias hist='history | grep'
alias ispark='IPYTHON_OPTS="notebook --pylab inline" ~/tech/spark-1.2.0-bin-hadoop2.4/bin/pyspark'
alias spark='/home/ophchu/tech/spark-1.2.0-bin-hadoop2.4/bin/spark-shell'
alias s3='aws s3'
ssh-emr(){
	ssh -A hadoop@$1
}
alias semr=ssh-emr
alias sshadd='eval `ssh-agent` && ssh-add ~/.ssh/opr-ophir.pem'
alias myt='tree -L 3 -d'
alias gits='git status -s -b' 
alias s3sync='aws s3 sync s3://ophir-test/user/ophirc/perres/ . --exclude "*/_SUCCESS"'
alias gos='cd  ~/work/opr-repos/opr-spark/'
alias vimal='vim ~/.bash_aliases; source ~/.bashrc'

alias spinit='cd ~/work/opr-repos/opr-dataloader/fabs/;fab spin_them_all:name='ophir-features-cluster'; cd -'
