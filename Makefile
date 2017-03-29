#$Id: Makefile,v 1.11 2012-04-17 19:30:40 aosorio Exp $
include make.configs

PARSER_CRONTAB=parser_crontab
INIT_TARGET=hicom_reader
TEMPLATE_TARGETS=reader_hicom300_conf.py logParser consulta_llamadas.php \
                 $(PARSER_CONFIG_FILE)  $(INIT_TARGET) $(PARSER_CRONTAB)
NORMAL_TARGETS=buffer_thread_safety.py reader_hicom300.py serial_conf.py \
               getLocation.py

% : %.template
	./instanciateMacros make.configs < $< > $@

.PHONY: all
all: install set_config

.PHONY: clean
clean:
	rm -f $(TEMPLATE_TARGETS)
        
.PHONY: install
install: $(TEMPLATE_TARGETS) $(NORMAL_TARGETS)
	mkdir -p $(WORKDIR)
	cp $(TEMPLATE_TARGETS) $(NORMAL_TARGETS) $(WORKDIR)
	chmod +x $(INIT_TARGET)
	cp $(INIT_TARGET) /etc/init.d
	update-rc.d -f $(INIT_TARGET) defaults
	mkdir -p $(PARSER_CONFIG_DIR)
	cp $(PARSER_CONFIG_FILE) $(PARSER_CONFIG_DIR)
	install -m 644 consulta_llamadas.php $(APACHE_DIR)
	install -m 644 style.css $(APACHE_DIR)
	install -m 755 logParser generarCopy $(USER_BIN_DIR)

.PHONY: set_config
set_config: $(TEMPLATE_TARGETS)
	install -m 775 -d $(PARSER_CONFIG_DIR)
	install -m 644 $(PARSER_CONFIG_FILE) $(PARSER_CONFIG_DIR)
	install -m 644 $(PARSER_CRONTAB) /etc/cron.d

.PHONY: createdb
createdb:
	createdb -EUTF-8 -U $(DBUSER) $(DBNAME)

.PHONY: rebuild
rebuild: destroy build

.PHONY: build
build:
	@{ echo "CREATE SCHEMA $(DBSCHEMA) ;" ; \
           echo "SET search_path=$(DBSCHEMA) ;" ; \
	   cat tablas.sql ; \
         } | psql -U $(DBUSER) $(DBNAME)

.PHONY: destroy
destroy:
	echo "DROP SCHEMA $(DBSCHEMA) CASCADE ;" | psql -U $(DBUSER) $(DBNAME)

.PHONY: destroydb
destroydb:
	dropdb $(DBNAME) -U $(DBUSER)
