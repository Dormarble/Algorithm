package main

import (
	"fmt"
	"log"
	"time"
)

var items []item

type item struct {
	no     int
	name   string
	point  int
	amount int
}
type buyer struct {
	point         int
	shoppingList  []item
	deliveryList  []delivery
	deliveryLimit int
}

func newBuyer() buyer {
	b := buyer{}
	b.point = 1000000
	b.shoppingList = []item{}
	b.deliveryList = []delivery{}
	b.deliveryLimit = 0

	return b
}
func (b *buyer) orderItem(i item) error {
	if i.amount > items[i.no].amount {
		err := fmt.Errorf("재고가 없습니다.")
		return err
	}
	if i.amount <= 0 {
		err := fmt.Errorf("유효하지 않은 수량입니다.")
		return err
	}
	if b.deliveryLimit >= 5 {
		err := fmt.Errorf("더이상 주문할 수 없습니다.")
		return err
	}
	if b.point < i.point*i.amount {
		err := fmt.Errorf("마일리지가 부족합니다.")
		return err
	}
	items[i.no].amount -= i.amount
	b.point -= i.point * i.amount
	b.deliveryList = append(b.deliveryList, delivery{i, ""})

	go b.deliveryList[len(b.deliveryList)-1].startDelivery(b)

	return nil
}
func (b *buyer) putList(i item) error {
	b.shoppingList = append(b.shoppingList, i)
	return nil
}
func (b buyer) commitDelivery() {
	if len(b.deliveryList) == 0 {
		fmt.Println("주문한 상품이 없습니다.")
	} else {
		for i, list := range b.deliveryList {
			fmt.Printf("%d. %10s\t%d\t%10s\n", i+1, list.orderedItem.name, list.orderedItem.amount, list.state)
		}
	}
}
func (b buyer) commitShoppingList() (listNum int) {
	listNum = len(b.shoppingList)
	for i, list := range b.shoppingList {
		fmt.Printf("%d. %10s\t%d", i, list.name, list.amount)
	}
	return
}
func (b *buyer) buyShoppingList() {
	tmpList := []item{}
	for _, i := range b.shoppingList {
		err := b.orderItem(i)
		if err != nil {
			tmpList = append(tmpList, i)
		}
	}
	b.shoppingList = tmpList
}

type delivery struct {
	orderedItem item
	state       string
}

func (d *delivery) startDelivery(b *buyer) {
	b.deliveryLimit++
	d.state = "주문접수"
	time.Sleep(time.Second * 10)

	d.state = "배송중"
	time.Sleep(time.Second * 30)

	d.state = "배송완료"
	time.Sleep(time.Second * 10)
	b.deliveryLimit--
}

func main() {
	var sel, sel2, selectedItemNum, amount int
	buyer := newBuyer()

	items = []item{}
	items = append(items, item{0, "텀블러", 10000, 30})
	items = append(items, item{1, "롱패딩", 500000, 20})
	items = append(items, item{2, "투미 백팩", 400000, 20})
	items = append(items, item{3, "나이키 운동화", 150000, 50})
	items = append(items, item{4, "빼빼로", 1200, 500})
	for {
		fmt.Println("1. 구매")
		fmt.Println("2. 잔여 수량 확인")
		fmt.Println("3. 잔여 마일리지 확인")
		fmt.Println("4. 배송 상태 확인")
		fmt.Println("5. 장바구니 확인")
		fmt.Println("6. 프로그램 종료")

		fmt.Scanln(&sel)

		switch sel {
		case 1:
			for {
				for i, item := range items {
					fmt.Printf("%d. %10s\t%7d\t\t%d\n", i, item.name, item.point, item.amount)
				}
				fmt.Print("구입할 상품을 선택해주세요: ")
				fmt.Scanln(&selectedItemNum)

				if selectedItemNum < 0 && len(items) <= selectedItemNum {
					log.Print("잘못된 상품 번호입니다.")
					continue
				}

				fmt.Print("구매할 수량을 선택해주세요: ")
				fmt.Scanln(&amount)

				fmt.Println("1. 바로주문")
				fmt.Println("2. 장바구니 담기")
				fmt.Scanln(&sel2)
				if sel2 != 1 && sel2 != 2 {
					fmt.Println("잘못된 입력입니다.")
					continue
				}
				item := item{items[selectedItemNum].no, items[selectedItemNum].name, items[selectedItemNum].point, amount}

				switch sel2 {
				case 1:
					err := buyer.orderItem(item)
					if err != nil {
						continue
					}
				case 2:
					err := buyer.putList(item)
					fmt.Print(buyer.shoppingList)
					if err != nil {
						continue
					}
				}
				break
			}
		case 2:
			for i, item := range items {
				fmt.Printf("%d. %10s\t%7d\t\t%d\n", i, item.name, item.point, item.amount)
			}
		case 3:
			fmt.Println("잔여 마일리지", buyer.point)
		case 4:
			buyer.commitDelivery()
		case 5:
			listNum := buyer.commitShoppingList()
			if listNum != 0 {
				fmt.Println("장바구니 상품들을 구매하시겠습니까?\n1.예  2.아니요")
				var sel3 int
				fmt.Scanln(&sel3)
				if sel3 == 1 {
					buyer.buyShoppingList()
					fmt.Println("주문 접수 되었습니다.")
				}
			} else {
				fmt.Println("장바구니가 비었습니다.")
			}
		case 6:
			return
		default:
			fmt.Println("잘못된 입력입니다.")
		}
	}
}
