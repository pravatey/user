package user

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

type Product struct {
	gorm.Model
	Code  string
	Price uint
}

func init() {
	db, _ := gorm.Open("postgres", "user=go dbname=gorm sslmode=disable")

	db.Create(&Product{Code: "L1212", Price: 1000})
	var product Product

	db.First(&product, 1)
	db.First(&product, "code = ?", "L1212")

	db.Model(&product).Update("Price", 2000)
}
