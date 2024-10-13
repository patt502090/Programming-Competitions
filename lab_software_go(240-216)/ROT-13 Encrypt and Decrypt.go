package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var opt int

	// แสดงตัวเลือก
	fmt.Println("Select 2 options")
	fmt.Println(" - 1 encrypt with ROT 13")
	fmt.Println(" - 2 decrypt with ROT 13\n")

	// รับตัวเลือกจากผู้ใช้
	fmt.Print("Choose option: ")
	fmt.Scan(&opt)

	// รับข้อความจากผู้ใช้
	fmt.Print("Enter text: ")
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)

	var result string

	// เข้ารหัสหรือถอดรหัสตามตัวเลือก
	for _, char := range input {
		if char >= 'A' && char <= 'Z' {
			// ROT13 สำหรับตัวอักษรใหญ่
			result += string('A' + (char-'A'+13)%26)
		} else if char >= 'a' && char <= 'z' {
			// ROT13 สำหรับตัวอักษรเล็ก
			result += string('a' + (char-'a'+13)%26)
		} else {
			// ตัวอักษรอื่นๆ ไม่เปลี่ยนแปลง
			result += string(char)
		}
	}

	// แสดงผลลัพธ์
	if opt == 1 {
		fmt.Printf("Ciphertext is \"%s\"\n", result)
	} else if opt == 2 {
		// สำหรับ ROT13 การเข้ารหัสและการถอดรหัสจะเหมือนกัน
		fmt.Printf("Plaintext is \"%s\"\n", result)
	} else {
		fmt.Println("Invalid option")
	}
}
