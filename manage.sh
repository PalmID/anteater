#!/usr/bin/env bash

FLASK_ENV=${FLASK_ENV:="development"}

db_host=${DB_HOST:="mysql"}
db_user=${DB_USER:="root"}
db_password=${DB_PASSWORD:="toor333666"}
db_name=${DB_NAME:="anteater"}
if [ ${FLASK_ENV} == "testing" ]; then
    db_name="tarot_test"
fi


date_str=$(date +"%Y_%m_%d_%H%M%S")
sql_basename="${date_str}_${FLASK_ENV}_${db_name}"

function orator_action() {
    migrations_path="db/migrations"
    case "$Action" in
        migrate )
            config_file="configs/${FLASK_ENV}.py"
            echo Using config file: ${config_file}
            before="${sql_basename}_ddl_before.sql"
            mysqldump_action ${before}
            PYTHONPATH=`pwd`:`pwd`/protos orator migrate -c ${config_file} -p ${migrations_path} $*
            # 即使migrate失败， 也有可能产生部分数据结构的改动
            after="${sql_basename}_ddl_after.sql"
            mysqldump_action ${after}
            echo "migrate前DDL文件: ${before}"
            echo "migrate后DDL文件: ${before}"
            echo "migrate前后DDL差异: "
            diff ${before} ${after}
            ;;
        make_migration)
            PYTHONPATH=`pwd`:`pwd`/protos orator make:migration -p ${migrations_path} $* ;;
        * ) ;;
    esac
}

function mysqldump_action() {
    mysqldump ${db_name} -u ${db_user} -h ${db_host} --password=${db_password} -r $*
}


Action=$1
shift

case "$Action" in
    make_migration | migrate )
        orator_action $* ;;

    * )
        echo 'Usage:'
        echo './manage.sh make_migration | migrate';;
esac
