class Solution:
    def addTwoNumbers(self, lista_1, lista_2):

        dummy = ListNode()
        atual = dummy
        carry = 0

        while lista_1 or lista_2 or carry:

            v1 = lista_1.val if lista_1 else 0

            v2 = lista_2.val if lista_2 else 0

            soma = v1 + v2 + carry

            carry = soma // 10

            atual.next = ListNode(soma % 10)

            atual = atual.next

            if lista_1:
                lista_1 = lista_1.next

            if lista_2:
                lista_2 = lista_2.next

        return dummy.next
