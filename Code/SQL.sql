CREATE TABLE "admin"."configura" ("pulsosvelcalc" INTEGER NULL, 
"tempovelcalc" FLOAT(8) NULL, 
"tempociclo" FLOAT(8) NULL, 
"grafpts" INTEGER NULL, 
"intvelfil" INTEGER NULL, 
"pwmfreq" FLOAT(8) NULL, 
"motorzm" FLOAT(8) NULL, 
"pwmzm" FLOAT(8) NULL);

CREATE TABLE "admin"."controle" ("ajuste" INTEGER NULL, 
"valork" FLOAT(8) NULL, 
"valorki" FLOAT(8) NULL, 
"valorkd" FLOAT(8) NULL, 
"fatora" FLOAT(8) NULL, 
"fatorb" FLOAT(8) NULL, 
"fatorc" FLOAT(8) NULL);

CREATE TABLE "admin"."dados" ("ajuste" FLOAT(8) NULL, 
"velocidade" FLOAT(8) NULL, 
"erro" FLOAT(8) NULL, 
"kp" FLOAT(8) NULL, 
"ki" FLOAT(8) NULL, 
"kd" FLOAT(8) NULL, 
"kmotor" FLOAT(8) NULL, 
"tempo" TIMESTAMP NULL);

INSERT INTO "admin"."configura" ("pulsosvelcalc", "tempovelcalc", "tempociclo", "grafpts", "intvelfil", "pwmfreq", "motorzm", "pwmzm") VALUES ('250','0,05','0,1','100','15','200','250','20');
INSERT INTO "admin"."controle" ("ajuste", "valork", "valorki", "valorkd", "fatora", "fatorb", "fatorc") VALUES ('0','1,9','0,02','0,005','0,0004','-0,1254','32,343');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','0','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:18');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','20,82080937216','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:18');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','66,2542219059222','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','119,096286733679','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','173,840129180041','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','229,680422074034','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','286,568850711069','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','343,32991396903','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','400,186008258576','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','456,860820567596','100','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','512,40085423954','96,1082087567337','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
INSERT INTO "admin"."dados" ("ajuste", "velocidade", "erro", "kp", "ki", "kd", "kmotor", "tempo") VALUES ('600','546,817546274138','91,0891078350215','1,5','0,5','0,05','7,2','26/07/2017 22:29:19');
