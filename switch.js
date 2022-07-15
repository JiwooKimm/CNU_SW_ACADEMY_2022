// console.log("Menu");
// console.log("1. Ice Americano");
// console.log("2. Cafe Latte");
// console.log("3. Cappucino");
// console.log("4. Tea");
// var choice = parseInt( prompt("메뉴 번호를 선택해 주세요 :)"));

// console.log( choice + '번 메뉴를 선택하셨습니다.');



// switch(choice){
// 	case 1:
// 		console.log('아이스 아메리카노는 1,500원 입니다.');
// 		break;
// 	case 2:
// 		console.log('카페 라떼는 1,800원 입니다.');
// 		break;
// 	case 3: 
// 		console.log('카푸치노는 2,000원 입니다.');
// 		break;
// 	case 4: 
// 		console.log('홍차는 1,300원 입니다.');
// 		break;
// 	default:
// 		console.log('메뉴를 다시 선택해주세요.');
// }







var apple = parseInt( prompt("🍎!\n랜덤 사과 뽑기를 합니다. \n1번 부터 10번까지의 사과 중 선택하세요: )"));
console.log(apple + '번 사과를 선택하셨습니다.');

switch(apple){
	case 1:
	case 5:
		console.log(apple + '번 사과는 썩은 사과입니다!');
		break;

	case 3:
		console.log(apple + '번 사과는 아이폰13pro입니다!');
		break;

	default:
		console.log(apple + '번 사과는 맛있는 사과입니다. 맛있게 드세요!');
}


