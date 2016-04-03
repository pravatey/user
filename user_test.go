package user

import "github.com/gin-gonic/gin"

func init() {
	r := GetRouter()
	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.Run()
}
