package user

import "github.com/gin-gonic/gin"

var r *gin.Engine

func GetRouter() *gin.Engine {
	if r == nil {
		r = gin.Default()
	}
	return r
}
