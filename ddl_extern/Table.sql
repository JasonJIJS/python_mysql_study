-- 판매가격순 정렬
select (select count(*) + 1 from sale_detail s2 where s2.sale_price > s1.sale_price) rank,
    sale.code doe, p.name name, price, salecnt, supply_price, addTax, sale_price, marginRate, margin_Price
    from sale inner join sale_detail s1 on sale.no = s1.no join product p on sale.code = p.code order by rank;



-- 마진액순 정렬
select (select count(*) + 1 from sale_detail s2 where s2.margin_Price > s1.margin_Price) rank,
    sale.code code, p.name name, price, salecnt, supply_price, addTax, sale_price, marginRate, margin_Price
    from sale inner join sale_detail s1 on sale.no = sale.no = s1.no join product p on sale.code = p.code order by rank;