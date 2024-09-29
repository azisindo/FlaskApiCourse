create table users (id int not null auto_increment,
                    name varchar(45),
                    email varchar(45),
                    phone varchar(45),
                    role varchar(45),
                    password varchar(45),
                    rold_id int(11),
                    primary key(id) );

select * from users;

insert into users values(1,'Awaludin Aziz','aziz.mcgr@gmail.com','082227919222','admin','12345') 

CREATE TABLE roles (id INT NOT NULL AUTO_INCREMENT,
					title VARCHAR(45),
                    primary key(id) );					
					);

ALTER TABLE users ADD role_id INT(11); 		

ALTER TABLE users ADD INDEX role_id_idx(role_id ASC);

ALTER TABLE users 
ADD CONSTRAINT role_id 
FOREIGN KEY (role_id)
REFERENCES roles(id)
ON DELETE NO ACTION
ON UPDATE CASCADE;

SELECT * FROM roles;

DELETE FROM roles WHERE id=13;

INSERT INTO roles values(1,'superadmin');

INSERT INTO roles values(12,'moderator');

INSERT INTO roles values(13,'user');

UPDATE users SET role_id=1 WHERE id=1; 

CREATE TABLE endpoints (id INT NOT NULL AUTO_INCREMENT,
                        endpoint VARCHAR(100),
                        methode VARCHAR(100),
                        PRIMARY KEY(id)
                        );
                       
INSERT INTO endpoints VALUES(1,'/user/getall','GET');

INSERT INTO endpoints VALUES(2,'/user/addone','POST');

INSERT INTO endpoints VALUES(3,'/user/update','PUT');

SELECT * FROM endpoints;

-- delete FROM endpoints;
                       COMMIT;

CREATE TABLE accessbility (id INT NOT NULL AUTO_INCREMENT,
                           endpoint_id INT(11),
                           roles LONGTEXT,
                           PRIMARY KEY (id)
                           );
                          
ALTER TABLE accessbility ADD INDEX endpoint_id_idx(endpoint_id ASC);
                          
ALTER TABLE accessbility 
ADD CONSTRAINT endpoint_id 
FOREIGN KEY (endpoint_id)
REFERENCES endpoints(id)
ON DELETE NO ACTION
ON UPDATE CASCADE;


INSERT INTO accessbility VALUES (1,1,'[1]');

INSERT INTO accessbility VALUES (4,2,'[]');

INSERT INTO accessbility VALUES (3,3,'[12,13]');

SELECT * FROM accessbility;

DELETE FROM accessbility WHERE id=2;

SELECT endpoint,
	   roles
FROM endpoints join accessbility
WHERE endpoints.id=accessbility.id;


CREATE VIEW accessbility_view as
SELECT endpoint,
	   roles
FROM endpoints join accessbility
WHERE endpoints.id=accessbility.id;

SELECT * FROM accessbility_view; 

SELECT * FROM accessbility_view where endpoint='/user/getall';
