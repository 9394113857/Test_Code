use dbim4u0mfuramq;

# User Table:-
select * from PATIENT_PERSONAL_DETAILS;
desc PATIENT_PERSONAL_DETAILS;


# Service Tables:-
select * from AMB_SITUATIONS;
select * from AMB_AMBULANCE_TYPES;
select * from AMB_ADVANCED_TYPES;
select * from AMB_CAUSES;

# Images Table:-
create table Images(
Id int primary key auto_increment,
file_name varchar(100),
mail_id varchar(50),
uploaded_on datetime
);
desc Images;

select * from Images;


