FROM mysql/mysql-server:5.7
ADD ./mysqld.cnf /etc/my.cnf
ADD ./entrypoint/db_template_with_vulns_pma_mwk_mgt_wordpress.sql /docker-entrypoint-initdb.d/db_template_with_vulns_pma_mwk_mgt_wordpress.sql
