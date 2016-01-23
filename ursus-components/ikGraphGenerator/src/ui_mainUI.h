/********************************************************************************
** Form generated from reading UI file 'mainUI.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINUI_H
#define UI_MAINUI_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_guiDlg
{
public:
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QGroupBox *initBox;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *fromFileButton;
    QPushButton *generateButton;
    QGroupBox *commandBox;
    QVBoxLayout *verticalLayout_2;
    QWidget *ikCommandWidget;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout_4;
    QVBoxLayout *verticalLayout_5;
    QSpacerItem *verticalSpacer_7;
    QSpacerItem *verticalSpacer_4;
    QLabel *label_8;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer_6;
    QLabel *label_7;
    QSpacerItem *verticalSpacer_2;
    QSpacerItem *verticalSpacer_5;
    QSpacerItem *verticalSpacer_8;
    QVBoxLayout *verticalLayout_4;
    QGridLayout *gridLayout_2;
    QLabel *label_5;
    QDoubleSpinBox *tz;
    QLabel *label_3;
    QLabel *label_4;
    QDoubleSpinBox *tx;
    QDoubleSpinBox *rx;
    QLabel *label;
    QLabel *label_2;
    QDoubleSpinBox *rz;
    QDoubleSpinBox *ry;
    QLabel *label_6;
    QDoubleSpinBox *ty;
    QCheckBox *checkBox;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *goIKButton;
    QPushButton *homeButton;
    QSpacerItem *verticalSpacer;
    QWidget *widget;

    void setupUi(QWidget *guiDlg)
    {
        if (guiDlg->objectName().isEmpty())
            guiDlg->setObjectName(QString::fromUtf8("guiDlg"));
        guiDlg->resize(972, 801);
        horizontalLayout = new QHBoxLayout(guiDlg);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        initBox = new QGroupBox(guiDlg);
        initBox->setObjectName(QString::fromUtf8("initBox"));
        horizontalLayout_2 = new QHBoxLayout(initBox);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        fromFileButton = new QPushButton(initBox);
        fromFileButton->setObjectName(QString::fromUtf8("fromFileButton"));

        horizontalLayout_2->addWidget(fromFileButton);

        generateButton = new QPushButton(initBox);
        generateButton->setObjectName(QString::fromUtf8("generateButton"));

        horizontalLayout_2->addWidget(generateButton);


        verticalLayout->addWidget(initBox);

        commandBox = new QGroupBox(guiDlg);
        commandBox->setObjectName(QString::fromUtf8("commandBox"));
        verticalLayout_2 = new QVBoxLayout(commandBox);
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        ikCommandWidget = new QWidget(commandBox);
        ikCommandWidget->setObjectName(QString::fromUtf8("ikCommandWidget"));
        verticalLayout_3 = new QVBoxLayout(ikCommandWidget);
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_7);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_4);

        label_8 = new QLabel(ikCommandWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        verticalLayout_5->addWidget(label_8);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_3);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_6);

        label_7 = new QLabel(ikCommandWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setLayoutDirection(Qt::LeftToRight);

        verticalLayout_5->addWidget(label_7);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_2);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_5);

        verticalSpacer_8 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_8);


        horizontalLayout_4->addLayout(verticalLayout_5);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(4);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(-1, 9, -1, -1);
        label_5 = new QLabel(ikCommandWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout_2->addWidget(label_5, 10, 0, 1, 1);

        tz = new QDoubleSpinBox(ikCommandWidget);
        tz->setObjectName(QString::fromUtf8("tz"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tz->sizePolicy().hasHeightForWidth());
        tz->setSizePolicy(sizePolicy);
        tz->setDecimals(1);
        tz->setMinimum(-2000);
        tz->setMaximum(2000);
        tz->setSingleStep(10);
        tz->setValue(400);

        gridLayout_2->addWidget(tz, 7, 0, 1, 1);

        label_3 = new QLabel(ikCommandWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_2->addWidget(label_3, 4, 0, 1, 1);

        label_4 = new QLabel(ikCommandWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_2->addWidget(label_4, 8, 0, 1, 1);

        tx = new QDoubleSpinBox(ikCommandWidget);
        tx->setObjectName(QString::fromUtf8("tx"));
        sizePolicy.setHeightForWidth(tx->sizePolicy().hasHeightForWidth());
        tx->setSizePolicy(sizePolicy);
        tx->setDecimals(1);
        tx->setMinimum(-2000);
        tx->setMaximum(2000);
        tx->setSingleStep(10);
        tx->setValue(200);

        gridLayout_2->addWidget(tx, 3, 0, 1, 1);

        rx = new QDoubleSpinBox(ikCommandWidget);
        rx->setObjectName(QString::fromUtf8("rx"));
        sizePolicy.setHeightForWidth(rx->sizePolicy().hasHeightForWidth());
        rx->setSizePolicy(sizePolicy);
        rx->setDecimals(3);
        rx->setMinimum(-10);
        rx->setMaximum(10);
        rx->setSingleStep(0.1);

        gridLayout_2->addWidget(rx, 9, 0, 1, 1);

        label = new QLabel(ikCommandWidget);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_2->addWidget(label, 2, 0, 1, 1);

        label_2 = new QLabel(ikCommandWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_2->addWidget(label_2, 6, 0, 1, 1);

        rz = new QDoubleSpinBox(ikCommandWidget);
        rz->setObjectName(QString::fromUtf8("rz"));
        sizePolicy.setHeightForWidth(rz->sizePolicy().hasHeightForWidth());
        rz->setSizePolicy(sizePolicy);
        rz->setDecimals(3);
        rz->setMinimum(-10);
        rz->setMaximum(10);
        rz->setSingleStep(0.1);
        rz->setValue(0);

        gridLayout_2->addWidget(rz, 13, 0, 1, 1);

        ry = new QDoubleSpinBox(ikCommandWidget);
        ry->setObjectName(QString::fromUtf8("ry"));
        sizePolicy.setHeightForWidth(ry->sizePolicy().hasHeightForWidth());
        ry->setSizePolicy(sizePolicy);
        ry->setDecimals(3);
        ry->setMinimum(-10);
        ry->setMaximum(10);
        ry->setSingleStep(0.1);
        ry->setValue(-1.571);

        gridLayout_2->addWidget(ry, 11, 0, 1, 1);

        label_6 = new QLabel(ikCommandWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout_2->addWidget(label_6, 12, 0, 1, 1);

        ty = new QDoubleSpinBox(ikCommandWidget);
        ty->setObjectName(QString::fromUtf8("ty"));
        sizePolicy.setHeightForWidth(ty->sizePolicy().hasHeightForWidth());
        ty->setSizePolicy(sizePolicy);
        ty->setDecimals(1);
        ty->setMinimum(-2000);
        ty->setMaximum(2000);
        ty->setSingleStep(10);
        ty->setValue(800);

        gridLayout_2->addWidget(ty, 5, 0, 1, 1);

        checkBox = new QCheckBox(ikCommandWidget);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));

        gridLayout_2->addWidget(checkBox, 14, 0, 1, 1);


        verticalLayout_4->addLayout(gridLayout_2);


        horizontalLayout_4->addLayout(verticalLayout_4);


        verticalLayout_3->addLayout(horizontalLayout_4);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        goIKButton = new QPushButton(ikCommandWidget);
        goIKButton->setObjectName(QString::fromUtf8("goIKButton"));

        horizontalLayout_3->addWidget(goIKButton);


        verticalLayout_3->addLayout(horizontalLayout_3);


        verticalLayout_2->addWidget(ikCommandWidget);

        homeButton = new QPushButton(commandBox);
        homeButton->setObjectName(QString::fromUtf8("homeButton"));

        verticalLayout_2->addWidget(homeButton);


        verticalLayout->addWidget(commandBox);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);


        horizontalLayout->addLayout(verticalLayout);

        widget = new QWidget(guiDlg);
        widget->setObjectName(QString::fromUtf8("widget"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy1);

        horizontalLayout->addWidget(widget);


        retranslateUi(guiDlg);

        QMetaObject::connectSlotsByName(guiDlg);
    } // setupUi

    void retranslateUi(QWidget *guiDlg)
    {
        guiDlg->setWindowTitle(QApplication::translate("guiDlg", "ikGraphGenerator", 0, QApplication::UnicodeUTF8));
        initBox->setTitle(QApplication::translate("guiDlg", "Initialization", 0, QApplication::UnicodeUTF8));
        fromFileButton->setText(QApplication::translate("guiDlg", "read graph\n"
"from file", 0, QApplication::UnicodeUTF8));
        generateButton->setText(QApplication::translate("guiDlg", "generate\n"
"new graph", 0, QApplication::UnicodeUTF8));
        commandBox->setTitle(QApplication::translate("guiDlg", "Command", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("guiDlg", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">T</span></p></body></html>", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("guiDlg", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">R</span></p></body></html>", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("guiDlg", "ry", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("guiDlg", "ty", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("guiDlg", "rx", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("guiDlg", "tx", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("guiDlg", "tz", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("guiDlg", "rz", 0, QApplication::UnicodeUTF8));
        checkBox->setText(QApplication::translate("guiDlg", "ignore\n"
"rotation", 0, QApplication::UnicodeUTF8));
        goIKButton->setText(QApplication::translate("guiDlg", "go target", 0, QApplication::UnicodeUTF8));
        homeButton->setText(QApplication::translate("guiDlg", "go home", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class guiDlg: public Ui_guiDlg {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINUI_H
