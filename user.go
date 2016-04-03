package user

import "github.com/gin-gonic/gin"

const (
	URL_USERS = "/users"
	URL_USER  = "/users/:userId"
)

type UsersHandler struct {
}

func (us *UsersHandler) GET(c *gin.Context) {
}

func (us *UsersHandler) POST(c *gin.Context) {
}

type UserHandler struct {
}

func (u *UserHandler) GET(c *gin.Context) {
}

func (u *UserHandler) PATCH(c *gin.Context) {
}

func (u *UserHandler) DELETE(c *gin.Context) {
}

func init() {
	r := GetRouter()

	r.GET(URL_USERS, &UsersHandler{}.get)
	r.POST(URL_USERS, &UsersHandler{}.post)
}
