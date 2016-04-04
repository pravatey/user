package user

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"github.com/mholt/binding"
)

const (
	URL_USERS = "/users"
	URL_USER  = "/users/:userId"
)

type UsersHandler struct {
}

//list users
func (us *UsersHandler) GET(c *gin.Context) {
	c.JSON(200, gin.H{
		"users": "a",
	})
}

type CreateUserModel struct {
	gorm.Model
	UserId   string
	Account  string
	Passwd   string
	Email    string
	Phone    string
	Portrait string
}

func (cf *CreateUserModel) FieldMap(req *http.Request) binding.FieldMap {
	return binding.FieldMap{
		&cf.Account: binding.Field{
			Form:     "account",
			Required: true,
		},
		&cf.Passwd: binding.Field{
			Form:     "passwd",
			Required: true,
		},
		&cf.Email:    "email",
		&cf.Phone:    "phone",
		&cf.Portrait: "portrait",
	}
}

//add user
func (us *UsersHandler) POST(c *gin.Context) {
	db := GetDB()
	createUserForm := new(CreateUserModel)
	errs := binding.Bind(c.Request, createUserForm)

	if errs.Handle(c.Writer) {
		fmt.Println("create user bind error")
		return
	}

	c.JSON(200, gin.H{
		"userId": 123,
	})
}

type UserHandler struct {
}

//get user info
func (u *UserHandler) GET(c *gin.Context) {
}

//update user info
func (u *UserHandler) PATCH(c *gin.Context) {
}

//delete user
func (u *UserHandler) DELETE(c *gin.Context) {
}

func init() {
	r := GetRouter()

	r.GET(URL_USERS, (&UsersHandler{}).GET)
	r.POST(URL_USERS, (&UsersHandler{}).POST)

	r.GET(URL_USER, (&UserHandler{}).GET)
	r.PATCH(URL_USER, (&UserHandler{}).PATCH)
	r.DELETE(URL_USER, (&UserHandler{}).DELETE)
}
