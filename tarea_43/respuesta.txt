# SQL

Las sentencia SQL utilizadas para cada caso resuelto junto con una breve explicación sobre la sentencia SQL utilizadas para resolver los problemas planteados en:

https://sqlpd.com/

## Respuestas

### 1.
White hat hacker has sent SQLPD exposed members' details of a shady site connected to various persons of interest.   
Please submit all members' details.    
Un hacker de sombrero blanco ha enviado a SQLPD los datos de los miembros expuestos de un sitio turbio relacionado con varias personas de interés. Por favor, envíe los detalles de todos los miembros.  

> SELECT * from users


### 2.
An illegal site's servers were seized in a recent operation. Please submit all users access times and number of downloads' details.  
***Los servidores de un sitio ilegal fueron incautados en una reciente operación.   
Por favor, envíe todos los datos de acceso de los usuarios y el número de descargas.***   

> SELECT AccessTime from users;

![](2.png)

### 3.
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all records first names and last names' details.  

***Se ha enviado una lista de correo de un servicio en línea ilegal a la línea directa del SQLPD. 
Por favor, envíe los datos de los nombres y apellidos de todos los registros.***  

> SELECT FirstName, LastName FROM mailing_list;

![](3.png)

### 4.
An illegal site's servers were seized in a recent operation. Please submit all users last access times, first names and last names' details.  
Los servidores de un sitio ilegal fueron incautados en una operación reciente. Por favor, envíen los datos de todos los usuarios de la última hora de acceso, nombres y apellidos.  

> SELECT LastAcces, Fistname, LastName FROM users;

![](4.png)

### 5.
An illegal site's servers were seized in a recent operation. Please submit all users last access times' details. Please make sure there are no duplicates.  
Los servidores de un sitio ilegal fueron incautados en una reciente operación. Por favor, envíe los datos de la última hora de acceso de todos los usuarios. Por favor, asegúrese de que no hay duplicados.  

> SELECT DISTINCT LastAccess FROM users;

![](5.png)

### 6.
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all entries' details sorted by number of password changes in ascending order.  
***Se ha enviado una lista de correo de un servicio en línea ilegal a la línea directa del SQLPD. 
Por favor, envíe los datos de todas las entradas ordenadas por número de cambios de contraseña en orden ascendente.*** 

> SELECT * FROM mailing_list ORDER BY passwordChanges;

![](6.png)

### 7. 
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all entries' details sorted by last names in descending order.
***Se ha enviado una lista de correo de un servicio en línea ilegal a la línea directa del SQLPD. 
Por favor, envíe los datos de todas las entradas ordenadas por apellidos en orden descendente.***

> SELECT * FORM mailing_list ORDER BY LastName DESC;

![](7.png)

### 8.
An illegal site's servers were seized in a recent operation. Please submit all users last names and number of posts' details sorted by number of posts in descending order. Please make sure there are no duplicates.
***Los servidores de un sitio ilegal fueron incautados en una reciente operación. Por favor, envíe todos los apellidos de los 
usuarios y el número de mensajes ordenados por número de mensajes en orden descendente. Por favor, asegúrese de que no hay duplicados.***

> SELECT DISTINCT Lastname, Post FROM users ORDER BY Post DESC;

![](8.png)

### 9.
An illegal site's servers were seized in a recent operation. Please submit all users family names, access times and given names' details sorted by access times in ascending order and then by given names in descending order.
***Los servidores de un sitio ilegal fueron incautados en una reciente operación. 
Por favor, envíe todos los nombres de familia de los usuarios, las horas de acceso y 
los detalles de los nombres de pila ordenados por horas de acceso en orden ascendente y luego por nombres de pila en orden descendente.***

> SELECT Familyname, AccessTime, GivenName FROM users ORDER BY AccessTime ASC, GivenName DESC;

![](9.png)

### 10.
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit the top 10 entries' details when sorted by given names in ascending order and then by email addresses in ascending order.
***Se ha enviado una lista de correo de un servicio en línea ilegal a la línea directa del SQLPD. Por favor, envíe los datos de las 10 primeras entradas clasificadas por nombres en orden ascendente y luego por direcciones de correo electrónico en orden ascendente.***

> SELECT * FORM mailing_list ORDER BY GivenName ASC, EmailAddress ASC LIMIT 10;

![](10.png)