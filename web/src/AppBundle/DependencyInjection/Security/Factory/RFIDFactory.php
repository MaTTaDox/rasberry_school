<?php

namespace AppBundle\DependencyInjection\Security\Factory;

use AppBundle\Security\Authentication\Provider\RFIDProvider;
use AppBundle\Security\Firewall\RFIDListener;
use Symfony\Component\DependencyInjection\ChildDefinition;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\DependencyInjection\Reference;
use Symfony\Component\Config\Definition\Builder\NodeDefinition;
use Symfony\Bundle\SecurityBundle\DependencyInjection\Security\Factory\SecurityFactoryInterface;

class RFIDFactory implements SecurityFactoryInterface
{
    public function create(ContainerBuilder $container, $id, $config, $userProvider, $defaultEntryPoint)
    {
        $providerId = 'security.authentication.provider.rfid.' . $id;
        $container
            ->setDefinition($providerId, new ChildDefinition(RFIDProvider::class))
            ->setArgument(0, new Reference($userProvider));

        $listenerId = 'security.authentication.listener.rfid.' . $id;
        $listener = $container->setDefinition($listenerId, new ChildDefinition(RFIDListener::class));

        return array($providerId, $listenerId, $defaultEntryPoint);
    }

    public function getPosition()
    {
        return 'pre_auth';
    }

    public function getKey()
    {
        return 'rfid';
    }

    public function addConfiguration(NodeDefinition $node)
    {
    }
}