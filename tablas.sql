/**
 * $Id: tablas.sql,v 1.3 2012-03-20 17:22:35 sshevtsov Exp $
 **
 * Tablas temporales para el parser.
 */

CREATE TABLE registro_de_llamada (
  fecha_de_llamada timestamp PRIMARY KEY,
  duracion interval,
  interno_de_origen numeric(3),
  numero_marcado varchar(100),
  estado_numero varchar(300)
) ;
