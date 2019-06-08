.global kaku
kaku:
    movq $0x00000001, %rax
    syscall
    retq

.global owaru
owaru:
    movq $0x0000003C, %rax
    syscall
