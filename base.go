package user

import (
	"fmt"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

var (
	r  *gin.Engine
	db *gorm.DB
)

func GetRouter() *gin.Engine {
	if r == nil {
		r = gin.Default()
	}
	return r
}

func GetDB() *gorm.DB {
	if db == nil {
		db, err := gorm.Open("postgres", "user=gorm dbname=gorm sslmode=disable")
		if err != nil {
			fmt.Println("Open data base failed")
			return
		}
	}
	return db
}
