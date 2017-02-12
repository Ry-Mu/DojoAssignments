JOINING TABLE ~

examples of joining tables:
1)Find all the clients(first and last name)billing amounts and charge date:
ERD - match client with billing
command:
    SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
    FROM clients
    JOIN billing ON clients.id = billing.clients_id;

2) list all the domain names and lead (first and last name) for each site
ERD - join sites with leads
command:
    SELECT site.domain_name, leads.first_name, leads.last_name
    FROM sites
    Join leads ON sites.id - leads.sites_id;

3) Join Multiple Tables Together
* Get the names of clients, their domain names and the first names of all the leads generated from those sites;
command:
    SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name AS leads_first
    FROM clients
    JOIN sites ON clients.id = sites.clients_id
    JOIN leads ON sites.id - leads.sites_id
- make sure find relationship and joining them clearly. * make sure the first name is clearified with the AS 'category'_first function.

4) Left and Right JOIN
- want something that doesn't really match with the right table
* List all the clients and the sites each client has, even if the client hasn't landed a site yet.
command:
SELECT client.first_name, clients.last_name, sites.domain_name
FROM clients
LEFT JOIN site ON clients.id = sites.clients_id;
* display everything on the left table even if it doesn't exist in the right table.
* if you change LEFT to RIGHT, vice versa. (usually don't happen if site will exist without client information, so mostly uses LEFT JOIN)

5) Group BY
* Find all the clients (first and last name) and their total billing amounts
command:
    SELECT clients.first_name, clients.last_name, SUM(billing.amount)
    FROM clients
    JOIN billing ON clients.id = billing.clients_id;
- say you want to sum up the total billing that one user has bought:
    GROUP BY clients.id;
    * Can use SUM as Min, Max, AVG etc.
- With GROUP BY, we will group multiple rows together, by performing a function to combine the values of those rows

6) Can also use CONCAT for groups:
    * List all the domain names associated with each client:
Command:
    SELECT GROUP_CONCAT(' ',sites.domain_name) AS domains, clients.first_name, clients.last_name
    FROM clients
    JOIN sites ON clients.id = sites.clients_id
    GROUP BY clients.id;

7)  Function
* find the total number of leads for each site.
command:
SELECT COUNT(leads.id), sites.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;
- just counting the rows from leads.id
- has single domain names with the leads.