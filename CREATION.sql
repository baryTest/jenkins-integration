create table emp
(
	noemp numeric not null,
	nom VARCHAR(20),
	prenom VARCHAR(20),
	emploi VARCHAR(20),
	sup numeric,
	embauche date,
	sal numeric,
	comm numeric,
	noserv numeric
);

alter table emp
add constraint PK_EMP primary key (noemp);


create table serv
(
noserv numeric not null,
service varchar(20),
ville varchar(20)
);

alter table serv
add constraint PK_SERV primary key(noserv);

insert into emp values (1000,'LEROY','PAUL','PRESIDENT',null,to_date('25/10/87','dd/MM/yy'),55005.5,null,1);
insert into emp values (1100,'DELPIERRE','DOROTHEE','SECRETAIRE',1000,to_date('25/10/87','dd/MM/yy'),12351.24,null,1);
insert into emp values (1101,'DUMONT','LOUIS','VENDEUR',1300,to_date('25/10/87','dd/MM/yy'),9047.9,0,1);
insert into emp values (1102,'MINET','MARC','VENDEUR',1300,to_date('25/10/87','dd/MM/yy'),8085.81,17230,1);
insert into emp values (1104,'NYS','ETIENNE','TECHNICIEN',1200,to_date('25/10/87','dd/MM/yy'),12342.23,null,1);
insert into emp values (1105,'DENIMAL','JEROME','COMPTABLE',1600,to_date('25/10/87','dd/MM/yy'),15746.57,null,1);
insert into emp values (1200,'LEMAIRE','GUY','DIRECTEUR',1000,to_date('11/03/87','dd/MM/yy'),36303.63,null,2);
insert into emp values (1201,'MARTIN','JEAN','TECHNICIEN',1200,to_date('25/06/87','dd/MM/yy'),11235.12,null,2);
insert into emp values (1202,'DUPONT','JACQUES','TECHNICIEN',1200,to_date('30/10/88','dd/MM/yy'),10313.03,null,2);
insert into emp values (1300,'LENOIR','GERARD','DIRECTEUR',1000,to_date('02/04/87','dd/MM/yy'),31353.14,13071,3);
insert into emp values (1301,'GERARD','ROBERT','VENDEUR',1300,to_date('16/04/99','dd/MM/yy'),7694.77,12430,3);
insert into emp values (1303,'MASURE','EMILE','TECHNICIEN',1200,to_date('17/06/88','dd/MM/yy'),10451.05,null,3);
insert into emp values (1500,'DUPONT','JEAN','DIRECTEUR',1000,to_date('23/10/87','dd/MM/yy'),28434.84,null,5);
insert into emp values (1501,'DUPIRE','PIERRE','ANALYSTE',1500,to_date('24/10/84','dd/MM/yy'),23102.31,null,5);
insert into emp values (1502,'DURAND','BERNARD','PROGRAMMEUR',1500,to_date('30/07/87','dd/MM/yy'),13201.32,null,5);
insert into emp values (1503,'DELNATTE','LUC','PUPITREUR',1500,to_date('15/01/99','dd/MM/yy'),8801.01,null,5);
insert into emp values (1600,'LAVARE','PAUL','DIRECTEUR',1000,to_date('13/12/91','dd/MM/yy'),31238.12,null,6);
insert into emp values (1601,'CARON','ALAIN','COMPTABLE',1600,to_date('16/09/85','dd/MM/yy'),33003.3,null,6);
insert into emp values (1602,'DUBOIS','JULES','VENDEUR',1300,to_date('20/12/90','dd/MM/yy'),9520.95,35535,6);
insert into emp values (1603,'MOREL','ROBERT','COMPTABLE',1600,to_date('18/07/85','dd/MM/yy'),33003.3,null,6);
insert into emp values (1604,'HAVET','ALAIN','VENDEUR',1300,to_date('01/01/91','dd/MM/yy'),9388.94,33415,6);
insert into emp values (1605,'RICHARD','JULES','COMPTABLE',1600,to_date('22/10/85','dd/MM/yy'),33503.35,null,5);
insert into emp values (1615,'DUPREZ','JEAN','BALAYEUR',1000,to_date('22/10/98','dd/MM/yy'),6000.6,null,5);

commit;


insert into serv values (1,'DIRECTION','PARIS');
insert into serv values (2,'LOGISTIQUE','SECLIN');
insert into serv values (3,'VENTES','ROUBAIX');
insert into serv values (4,'FORMATION','VILLENEUVE D''ASCQ');
insert into serv values (5,'INFORMATIQUE','LILLE');
insert into serv values (6,'COMPTABILITE','LILLE');
insert into serv values (7,'TECHNIQUE','ROUBAIX');


commit;

commit;
/* un bloc de commentaire */
-- 1. Afficher la table emp (en requete SQL) 
select * 
from emp;
 
-- 1 : S??lectionner toutes les colonnes de la table SERV.
SELECT * from serv;
-- 2 : S??lectionner d???une autre mani??re ces colonnes.

-- 3 : S??lectionner les colonnes SERVICE et NOSERV de la table  SERV.
SELECT service, noserv FROM serv;
-- 4 : S??lectionner toutes les colonnes de la table EMP.
SELECT nom, prenom, emploi, embauche, sup FROM emp; 
-- 5 : S??lectionner les emplois de la table EMP.

SELECT  emplois from emp;
-- 6 : S??lectionner les diff??rents emplois de la table EMP.
SELECT DISTINCT emploi from emp;

SELECT * from serv;
SELECT prenom from emp;
SELECT embauche from emp;

SELECT * from emp where nom is NULL;

SELECT * from emp where noemp ='1000';


-- SELECT AVEC CLAUSE WHERE : Pr??dicats simples
-- 7 : S??lectionner les employ??s du service N??3.
SELECT *from emp where noserv = '3';
-- 8 : S??lectionner les noms, pr??noms, num??ro d???employ??, num??ro  de service de tous les techniciens.
SELECT nom, noserv from emp where  emploi = 'TECHNICIEN';
-- 9 : S??lectionner les noms, num??ros de service de tous les services  dont le num??ro est sup??rieur ?? 2.
SELECT nom, noserv from emp where noserv > 2;
-- 10 : S??lectionner les noms, num??ros de service de tous les  services dont le num??ro est inf??rieur ou ??gal ?? 2.
SELECT nom, noserv from emp where noserv <=2 ;
-- 11 : S??lectionner les employ??s dont la commission est inf??rieure  au salaire. V??rifiez le r??sultat jusqu????? obtenir la bonne r??ponse.
SELECT *from emp where  coalesce(comm,0) <sal;


-- 12 : S??lectionner les employ??s qui ne touchent jamais de  commission.
SELECT *from emp where comm is NULL;

-- 13 : S??lectionner les employ??s qui touchent ??ventuellement une  commission et dans l???ordre croissant des commissions.

SELECT *from emp  ORDER BY comm;

-- 14 : S??lectionner les employ??s qui ont un chef.
SELECT *from emp where sup is not NULL;
-- 15 : S??lectionner les employ??s qui n???ont pas de chef.

SELECT *from  emp WHERE sup is NULL;
--16 : S??lectionner les noms, emploi, salaire, num??ro de service de tous les  employ??s du service 5 qui gagnent plus de 20000 ???.
SELECT nom, emploi, sal, noserv from emp where noserv = 5 and (sal +coalesce(comm,0)) >20000;
--17 : S??lectionner les vendeurs du service 6 qui ont un revenu mensuel  sup??rieur ou ??gal ?? 9500 ???.
SELECT  *from emp where  noserv = 6 and (sal +coalesce(comm,0)/12)>= 9500;
--18 : S??lectionner dans les employ??s tous les pr??sidents et directeurs.  Attention, le fran??ais et la logique sont parfois contradictoires.
select  * from emp where  emploi ='PRESIDENT' OR emploi ='DIRECTEUR';
--19 : S??lectionner les directeurs qui ne sont pas dans le service 3.
SELECT *from emp where emploi ='DIRECTEUR' and  noserv != 3;
--20 : S??lectionner les directeurs et ?? les techniciens du service 1 ??.
SELECT *from emp WHERE emploi ='DIRECTEUR' or emploi ='TECHNICIEN' and noserv = 1;
--21 : S??lectionner les ?? directeurs et les techniciens ?? du service 1.
SELECT *from emp WHERE  noserv = 1 and (emploi ='DIRECTEUR' or emploi ='TECHNICIEN' );
--22 : S??lectionner les employ??s du service 1 qui sont directeurs ou techniciens.
SELECT *from emp where  emploi ='DIRECTEUR' or emploi ='TECHNICIEN' and noserv = 1;
--23 : S??lectionner les employ??s qui ne sont ni directeur, ni technicien et  travaillant dans le service 1.
SELECT *from emp where not(emploi= 'DIRECTEUR'and emploi='TECHNICIEN') and noserv = 1;
--24 : S??lectionner les employ??s qui sont techniciens, comptables ou vendeurs.
SELECT *from emp where emploi ='TECHNICIEN'or emploi='COMPTABLE'or emploi ='VENDEUR';
--25 : S??lectionner les employ??s qui ne sont ni technicien, ni comptable, ni vendeur.
SELECT *from emp where not (emploi ='TECHNICIEN'or emploi='COMPTABLE'or emploi ='VENDEUR');
--26 : S??lectionner les directeurs des services 2, 4 et 5.
SELECT *from emp where emploi ='DIRECTEUR' and noserv in (2, 4, 5);
--27 : S??lectionner les subalternes qui ne sont pas dans les services 1, 3, 5.
SELECT *from emp where sup is not null and noserv not in  (1, 3, 5);
--28 : S??lectionner les employ??s qui gagnent entre 20000 et 40000 euros, bornes comprises.
SELECT *,  (sal +coalesce(comm,0)) as revenu from emp where (sal +coalesce(comm,0)) between 20000 and 40000;
--29 : S??lectionner les employ??s qui gagnent moins de 20000 et plus de 40000 euros.
SELECT *,  (sal +coalesce(comm,0)) as revenu from emp where (sal +coalesce(comm,0)) < 20000 or sal > 40000;
--30 : S??lectionner les employ??s qui ne sont pas directeur et qui ont ??t?? embauch??s en 88.
SELECT *from  emp where emploi != 'DIRECTEUR'  and to_char(embauche, 'yy') like '%88';
--31 : S??lectionner les directeurs des services 2 ,3 , 4, 5 sans le IN.
SELECT *from emp where emploi ='DIRECTEUR' and noserv between  2 and   5;
--32 :S??lectionner les employ??s dont le nom commence par la lettre M.
SELECT *from emp where nom like 'M%';
--33 : S??lectionner les employ??s dont le nom se termine par T.
SELECT *from emp where nom like '%T';
--34 : S??lectionner les employ??s ayant au moins deux E dans leur nom.
SELECT *from emp where nom like '%E%E%'; 
--35 : S??lectionner les employ??s ayant exactement un E dans leur nom.
SELECT *from emp where nom like '%E%' and not nom like '%E%E%';
--36 : S??lectionner les employ??s ayant au moins un N et un O dans leur nom.
SELECT *from emp where nom  like '%E%' and  nom like '%O%';
--37 : S??lectionner les employ??s dont le nom s'??crit avec 6 caract??res et qui se termine par N.
SELECT *from emp where nom like '____N';
--38 : S??lectionner les employ??s dont la troisi??me lettre du nom est un R.
SELECT *from emp where nom like '__R%';

--39 : S??lectionner les employ??s dont le nom ne s'??crit pas avec 5 caract??res.
SELECT *from emp where nom not like '_____';

/*ou*/
SELECT *from emp where LENGTH(nom)<> 5;
--40 : Trier les employ??s (nom, pr??nom, n?? de service, salaire) du service 3 par  ordre de salaire croissant.
SELECT nom, prenom, noserv, sal from emp where noserv = 3 ORDER BY sal ASC ;
--41 : Trier les employ??s (nom, pr??nom, n?? de service , salaire) du service 3  par ordre de salaire d??croissant.
SELECT nom, prenom, noserv, sal from emp where noserv = 3 ORDER BY sal DESC; 
--42 : Idem en indiquant le num??ro de colonne ?? la place du nom colonne.
SELECT nom, prenom, noserv, sal from emp where noserv = 3 ORDER BY 4 DESC;
--43 : Trier les employ??s (nom, pr??nom, n?? de service, salaire, emploi) par  emploi, et pour chaque emploi par ordre d??croissant de salaire.
SELECT nom, prenom, noserv, sal, emploi from emp  ORDER BY emploi, sal DESC;
--44 : Idem en indiquant les num??ros de colonnes.
SELECT nom, prenom, noserv, sal, emploi from emp  ORDER BY emploi, sal, 4 DESC;
--45 : Trier les employ??s (nom, pr??nom, n?? de service, commission) du service  3 par ordre croissant de commission.
--46 : Trier les employ??s (nom, pr??nom, n?? de service, commission) du service  3 par ordre d??croissant de commission, en consid??rant que celui dont la  commission est nulle ne touche pas de commission.

